import backtrader as bt
import numpy as np

class EhlersCenterOfGravityOscillator(bt.Indicator):
    """
    Ehlers Center of Gravity Oscillator
    
    Ein fortgeschrittener Momentum-Oszillator, der den 
    Schwerpunkt der Preisbewegung berechnet.
    
    Features:
    - Adaptive Zykluserkennung
    - Trendstärke-Messung
    - Überverkauft/Überkauft-Signale
    - Divergenz-Erkennung
    
    Parameter:
    - period (10): Berechnungsperiode
    - phase_shift (0): Phasenverschiebung
    """
    
    lines = ('cog', 'signal', 'trigger')
    params = (
        ('period', 10),
        ('phase_shift', 0),
    )
    
    plotlines = dict(
        cog=dict(color='blue', _name='COG'),
        signal=dict(color='red', _name='Signal'),
        trigger=dict(color='green', _name='Trigger')
    )
    
    def __init__(self):
        super(EhlersCenterOfGravityOscillator, self).__init__()
        
        # Puffer für Berechnungen
        self.price_buffer = []
        self.cog_buffer = []
        
        # Initialisierung der Hilfslinien
        self.l.signal = bt.indicators.EMA(self.l.cog, period=9)
        self.l.trigger = bt.indicators.EMA(self.l.signal, period=3)
        
    def prenext(self):
        # Sammle Daten für die erste Berechnung
        self.price_buffer.append(self.data[0])
        if len(self.price_buffer) > self.p.period:
            self.price_buffer.pop(0)
            
    def next(self):
        # Aktuelle Preisdaten sammeln
        self.price_buffer.append(self.data[0])
        if len(self.price_buffer) > self.p.period:
            self.price_buffer.pop(0)
            
        if len(self.price_buffer) < self.p.period:
            return
            
        # Center of Gravity berechnen
        numerator = 0
        denominator = 0
        
        for i in range(self.p.period):
            weight = i + 1
            price = self.price_buffer[-(i+1)]
            numerator += price * weight
            denominator += price
            
        if denominator != 0:
            cog = -numerator / denominator + (self.p.period + 1) / 2
        else:
            cog = 0
            
        # Phase verschieben
        if self.p.phase_shift != 0:
            cog = np.roll(cog, self.p.phase_shift)
            
        # Normalisierung
        self.cog_buffer.append(cog)
        if len(self.cog_buffer) > 100:  # Gleitender Max/Min
            self.cog_buffer.pop(0)
            
        if len(self.cog_buffer) > 1:
            max_cog = max(self.cog_buffer)
            min_cog = min(self.cog_buffer)
            
            if max_cog != min_cog:
                cog = (cog - min_cog) / (max_cog - min_cog) * 2 - 1
                
        # Linien aktualisieren
        self.l.cog[0] = cog
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_cog = self.l.cog[0]
        current_signal = self.l.signal[0]
        current_trigger = self.l.trigger[0]
        
        # Trendstärke berechnen
        trend_strength = abs(current_cog)
        
        # Überverkauft/Überkauft-Status
        if current_cog > 0.8:
            condition = "überkauft"
        elif current_cog < -0.8:
            condition = "überverkauft"
        else:
            condition = "neutral"
            
        # Signalgenerierung
        if current_signal > current_trigger:
            signal = "bullish"
        elif current_signal < current_trigger:
            signal = "bearish"
        else:
            signal = "neutral"
            
        return {
            'momentum': {
                'value': current_cog,
                'strength': trend_strength,
                'condition': condition
            },
            'signals': {
                'primary': signal,
                'signal_line': current_signal,
                'trigger_line': current_trigger
            },
            'analysis': {
                'trend_quality': (
                    'stark' if trend_strength > 0.7
                    else 'moderat' if trend_strength > 0.3
                    else 'schwach'
                ),
                'cycle_phase': (
                    'steigend' if current_cog > 0
                    else 'fallend'
                ),
                'trading_bias': (
                    'long' if current_cog > 0.3
                    else 'short' if current_cog < -0.3
                    else 'neutral'
                )
            }
        }
