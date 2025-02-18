import backtrader as bt
import numpy as np
from enum import Enum

class RiskLevel(Enum):
    """Risiko-Level-Klassifikation"""
    VERY_LOW = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    VERY_HIGH = 5

class RiskRewardRatioIndicator(bt.Indicator):
    """
    Risk-Reward Ratio Indicator
    
    Ein fortgeschrittener Indikator zur Analyse des
    Risiko-Ertrags-Verhältnisses.
    
    Features:
    - Dynamische R/R-Berechnung
    - Volatilitätsanalyse
    - Positionsgrößenoptimierung
    - Risikobewertung
    - Stop-Loss-Optimierung
    
    Parameter:
    - atr_period (14): ATR-Periode
    - risk_threshold (2.0): Risiko-Schwelle
    - target_rr (2.0): Ziel-R/R-Ratio
    """
    
    lines = ('rr_ratio', 'risk_level', 'position_size')
    params = (
        ('atr_period', 14),
        ('risk_threshold', 2.0),
        ('target_rr', 2.0),
    )
    
    plotlines = dict(
        rr_ratio=dict(color='blue', _name='R/R Ratio'),
        risk_level=dict(color='red', _name='Risk Level'),
        position_size=dict(color='green', _name='Position Size')
    )
    
    def __init__(self):
        super(RiskRewardRatioIndicator, self).__init__()
        
        # Volatilitätsindikatoren
        self.atr = bt.indicators.ATR(
            self.data,
            period=self.p.atr_period
        )
        self.bbands = bt.indicators.BollingerBands(
            self.data,
            period=20
        )
        
        # Trend-Indikatoren
        self.sma50 = bt.indicators.SMA(self.data, period=50)
        self.sma200 = bt.indicators.SMA(self.data, period=200)
        
        # Momentum-Indikatoren
        self.rsi = bt.indicators.RSI(self.data, period=14)
        
        # Puffer für Berechnungen
        self.risk_history = []
        self.reward_history = []
        
    def calculate_risk_level(self):
        """Berechnet das aktuelle Risiko-Level"""
        # Volatilitätsbasiertes Risiko
        vol_risk = self.atr[0] / self.data.close[0]
        
        # Trend-basiertes Risiko
        trend_risk = abs(
            self.sma50[0] - self.sma200[0]
        ) / self.data.close[0]
        
        # Momentum-basiertes Risiko
        mom_risk = abs(50 - self.rsi[0]) / 50
        
        # Gewichtetes Gesamtrisiko
        total_risk = (
            0.4 * vol_risk +
            0.3 * trend_risk +
            0.3 * mom_risk
        )
        
        # Risiko-Level bestimmen
        if total_risk < 0.02:
            return RiskLevel.VERY_LOW
        elif total_risk < 0.04:
            return RiskLevel.LOW
        elif total_risk < 0.06:
            return RiskLevel.MODERATE
        elif total_risk < 0.08:
            return RiskLevel.HIGH
        else:
            return RiskLevel.VERY_HIGH
            
    def calculate_optimal_position_size(self, risk_level):
        """Berechnet optimale Positionsgröße"""
        # Basis-Positionsgröße
        base_size = 1.0
        
        # Risiko-basierte Anpassung
        risk_factor = {
            RiskLevel.VERY_LOW: 1.0,
            RiskLevel.LOW: 0.8,
            RiskLevel.MODERATE: 0.6,
            RiskLevel.HIGH: 0.4,
            RiskLevel.VERY_HIGH: 0.2
        }[risk_level]
        
        # Volatilitätsanpassung
        vol_adjustment = 1.0 - (
            self.atr[0] / self.data.close[0]
        )
        
        # Trend-Anpassung
        trend_strength = abs(
            self.sma50[0] - self.sma200[0]
        ) / self.data.close[0]
        trend_adjustment = 1.0 - trend_strength
        
        # Finale Positionsgröße
        position_size = (
            base_size *
            risk_factor *
            vol_adjustment *
            trend_adjustment
        )
        
        return max(0.1, min(1.0, position_size))
        
    def calculate_rr_ratio(self, risk_level):
        """Berechnet das Risiko-Ertrags-Verhältnis"""
        # ATR-basierter Stop-Loss
        stop_distance = self.atr[0] * risk_level.value
        
        # Potentieller Verlust
        risk = stop_distance
        
        # Potentieller Gewinn (basierend auf Bollinger Bands)
        if self.data.close[0] < self.bbands.lines.bot[0]:
            # Überverkauft - höheres Gewinnpotential
            reward = self.bbands.lines.top[0] - self.data.close[0]
        elif self.data.close[0] > self.bbands.lines.top[0]:
            # Überkauft - niedrigeres Gewinnpotential
            reward = self.data.close[0] - self.bbands.lines.bot[0]
        else:
            # Neutraler Bereich
            reward = self.bbands.lines.mid[0] - self.data.close[0]
            
        if risk == 0:
            return 0
            
        return abs(reward / risk)
        
    def next(self):
        # Risiko-Level berechnen
        risk_level = self.calculate_risk_level()
        
        # R/R-Ratio berechnen
        rr_ratio = self.calculate_rr_ratio(risk_level)
        
        # Positionsgröße optimieren
        position_size = self.calculate_optimal_position_size(
            risk_level
        )
        
        # Historie aktualisieren
        self.risk_history.append(risk_level.value)
        self.reward_history.append(rr_ratio)
        
        # Maximal 100 Einträge speichern
        if len(self.risk_history) > 100:
            self.risk_history.pop(0)
        if len(self.reward_history) > 100:
            self.reward_history.pop(0)
            
        # Linien aktualisieren
        self.lines.rr_ratio[0] = rr_ratio
        self.lines.risk_level[0] = risk_level.value
        self.lines.position_size[0] = position_size
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_rr = self.lines.rr_ratio[0]
        current_risk = RiskLevel(int(self.lines.risk_level[0]))
        current_size = self.lines.position_size[0]
        
        return {
            'risk_analysis': {
                'level': current_risk.name,
                'value': current_risk.value,
                'trend': (
                    'steigend'
                    if len(self.risk_history) > 1 and
                    self.risk_history[-1] >
                    self.risk_history[-2]
                    else 'fallend'
                    if len(self.risk_history) > 1 and
                    self.risk_history[-1] <
                    self.risk_history[-2]
                    else 'stabil'
                )
            },
            'reward_analysis': {
                'rr_ratio': current_rr,
                'quality': (
                    'ausgezeichnet' if current_rr > 3
                    else 'gut' if current_rr > 2
                    else 'akzeptabel' if current_rr > 1
                    else 'schlecht'
                ),
                'trend': (
                    'verbessernd'
                    if len(self.reward_history) > 1 and
                    self.reward_history[-1] >
                    self.reward_history[-2]
                    else 'verschlechternd'
                    if len(self.reward_history) > 1 and
                    self.reward_history[-1] <
                    self.reward_history[-2]
                    else 'stabil'
                )
            },
            'position_sizing': {
                'recommended_size': current_size,
                'confidence': (
                    'hoch' if current_size > 0.8
                    else 'mittel' if current_size > 0.5
                    else 'niedrig'
                )
            },
            'trading_recommendation': {
                'action': (
                    'aggressive_entry'
                    if (current_rr > self.p.target_rr and
                        current_risk in [RiskLevel.VERY_LOW,
                                       RiskLevel.LOW])
                    else 'careful_entry'
                    if (current_rr > self.p.target_rr and
                        current_risk == RiskLevel.MODERATE)
                    else 'wait'
                    if current_rr < self.p.target_rr
                    else 'avoid'
                    if current_risk in [RiskLevel.HIGH,
                                      RiskLevel.VERY_HIGH]
                ),
                'stop_loss': self.atr[0] * current_risk.value,
                'take_profit': (
                    self.atr[0] * current_risk.value *
                    current_rr
                )
            },
            'market_conditions': {
                'volatility': (
                    'hoch' if self.atr[0] /
                    self.data.close[0] > 0.02
                    else 'moderat' if self.atr[0] /
                    self.data.close[0] > 0.01
                    else 'niedrig'
                ),
                'trend_strength': (
                    'stark' if abs(
                        self.sma50[0] - self.sma200[0]
                    ) / self.data.close[0] > 0.05
                    else 'moderat' if abs(
                        self.sma50[0] - self.sma200[0]
                    ) / self.data.close[0] > 0.02
                    else 'schwach'
                )
            }
        }
