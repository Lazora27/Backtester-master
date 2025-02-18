import backtrader as bt
import logging

logger = logging.getLogger(__name__)

class IndicatorHandler:
    def __init__(self, strategy=None):
        """
        Initialisiere den IndicatorHandler
        
        Args:
            strategy: Backtrader Strategy Instanz (optional)
        """
        self.strategy = strategy
        
    def create_indicator(self, name: str, **params) -> bt.Indicator:
        """
        Erstelle einen Indikator basierend auf Namen und Parametern
        
        Args:
            name: Name des Indikators
            **params: Parameter für den Indikator
            
        Returns:
            bt.Indicator: Der erstellte Indikator
        """
        try:
            if name == 'RSI':
                return bt.indicators.RSI(
                    self.strategy.data,
                    period=params.get('period', 14),
                    upperband=params.get('upperband', 70),
                    lowerband=params.get('lowerband', 30)
                )
            elif name == 'MACD':
                return bt.indicators.MACD(
                    self.strategy.data,
                    period_me1=params.get('period_me1', 12),
                    period_me2=params.get('period_me2', 26),
                    period_signal=params.get('period_signal', 9)
                )
            elif name == 'Stochastic':
                return bt.indicators.Stochastic(
                    self.strategy.data,
                    period=params.get('period', 14),
                    period_dfast=params.get('period_dfast', 3),
                    period_dslow=params.get('period_dslow', 3)
                )
            elif name == 'BollingerBands':
                return bt.indicators.BollingerBands(
                    self.strategy.data,
                    period=params.get('period', 20),
                    devfactor=params.get('devfactor', 2)
                )
            else:
                logger.error(f"Unbekannter Indikator: {name}")
                return None
                
        except Exception as e:
            logger.error(f"Fehler beim Erstellen von {name}: {str(e)}")
            return None
            
    def get_signal(self, name: str, indicator: bt.Indicator) -> float:
        """
        Berechne das Handelssignal für einen Indikator
        
        Args:
            name: Name des Indikators
            indicator: Indikator-Instanz
            
        Returns:
            float: Signal zwischen -1 und 1
        """
        try:
            if name == 'RSI':
                value = indicator[0]
                if value > 70:
                    return -1.0  # Überkauft
                elif value < 30:
                    return 1.0   # Überverkauft
                else:
                    # Normalisiere zwischen -1 und 1
                    return 2 * ((value - 50) / 50)  # Verwende feste Grenzen
                    
            elif name == 'MACD':
                if not indicator.macd or not indicator.signal:
                    return 0
                    
                macd = indicator.macd[0]
                signal = indicator.signal[0]
                
                # Normalisiere die Differenz
                if abs(signal) < 0.0001:  # Vermeide Division durch sehr kleine Zahlen
                    return 0
                    
                diff = macd - signal
                norm_diff = diff / abs(signal)
                return max(-1.0, min(1.0, norm_diff))
                
            elif name == 'Stochastic':
                k = indicator.percK[0]
                d = indicator.percD[0]
                
                if k > 80 and d > 80:
                    return -1.0
                elif k < 20 and d < 20:
                    return 1.0
                else:
                    # Normalisiere zwischen -1 und 1
                    return 2 * ((k - 50) / 50)  # Verwende feste Grenzen
                    
            elif name == 'BollingerBands':
                if not indicator.top or not indicator.bot or not indicator.mid:
                    return 0
                    
                price = self.strategy.data.close[0]
                top = indicator.top[0]
                bot = indicator.bot[0]
                mid = indicator.mid[0]
                
                # Berechne relative Position im Band
                band_width = top - bot
                if band_width < 0.0001:  # Vermeide Division durch sehr kleine Zahlen
                    return 0
                    
                relative_pos = (price - mid) / (band_width / 2)
                return max(-1.0, min(1.0, -relative_pos))  # Invertiere das Signal
                
            else:
                logger.error(f"Unbekannter Indikator für Signal: {name}")
                return 0
                
        except Exception as e:
            logger.error(f"Fehler bei Signal-Berechnung für {name}: {str(e)}")
            return 0
