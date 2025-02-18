import backtrader as bt
import numpy as np

class EhlersInstantaneousTrendline(bt.Indicator):
    """
    Ehlers Instantaneous Trendline
    
    Ein adaptiver Trendfolge-Indikator, der schnell auf
    Trendänderungen reagiert.
    
    Features:
    - Adaptive Trendberechnung
    - Rauschfilterung
    - Trendstärke-Messung
    - Frühe Trendwendesignale
    
    Parameter:
    - alpha (0.07): Glättungsfaktor
    - dc_period (20): Dominante Zyklusperiode
    """
    
    lines = ('trendline', 'trigger', 'slope')
    params = (
        ('alpha', 0.07),
        ('dc_period', 20),
    )
    
    plotlines = dict(
        trendline=dict(color='blue', _name='Trendline'),
        trigger=dict(color='red', _name='Trigger'),
        slope=dict(color='green', _name='Slope')
    )
    
    def __init__(self):
        super(EhlersInstantaneousTrendline, self).__init__()
        
        # Initialisierung der Puffer
        self.price_buffer = []
        self.it_buffer = []
        self.trigger_buffer = []
        
        # Hilfslinien
        self.l.trigger = self.l.trendline(-2)  # 2-Perioden Verzögerung
        
    def prenext(self):
        # Sammle initiale Daten
        self.price_buffer.append(self.data[0])
        if len(self.price_buffer) > self.p.dc_period:
            self.price_buffer.pop(0)
            
    def next(self):
        # Aktuelle Preisdaten sammeln
        self.price_buffer.append(self.data[0])
        if len(self.price_buffer) > self.p.dc_period:
            self.price_buffer.pop(0)
            
        if len(self.price_buffer) < 4:  # Mindestens 4 Perioden benötigt
            return
            
        # Instantaneous Trendline berechnen
        price = self.data[0]
        prev_price = self.data[-1]
        
        if not self.it_buffer:  # Erste Berechnung
            it = price
        else:
            prev_it = self.it_buffer[-1]
            
            # Adaptive Glättung
            smooth_factor = self.p.alpha
            if len(self.it_buffer) > 1:
                # Trendstärke berücksichtigen
                trend_strength = abs(
                    self.it_buffer[-1] - self.it_buffer[-2]
                )
                smooth_factor *= (1 + trend_strength)
                
            it = (
                (1 - smooth_factor) * prev_it +
                smooth_factor * (
                    (2 * price + prev_price) / 3
                )
            )
            
        self.it_buffer.append(it)
        if len(self.it_buffer) > self.p.dc_period:
            self.it_buffer.pop(0)
            
        # Steigung berechnen
        if len(self.it_buffer) > 1:
            slope = self.it_buffer[-1] - self.it_buffer[-2]
        else:
            slope = 0
            
        # Trigger-Line (verzögerte Trendline)
        if len(self.it_buffer) > 2:
            trigger = self.it_buffer[-3]  # 2-Perioden Verzögerung
            self.trigger_buffer.append(trigger)
            if len(self.trigger_buffer) > self.p.dc_period:
                self.trigger_buffer.pop(0)
        else:
            trigger = it
            
        # Linien aktualisieren
        self.l.trendline[0] = it
        self.l.trigger[0] = trigger
        self.l.slope[0] = slope
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        current_trend = self.l.trendline[0]
        current_trigger = self.l.trigger[0]
        current_slope = self.l.slope[0]
        
        # Trendstärke berechnen
        if len(self.it_buffer) > 1:
            trend_strength = abs(
                self.it_buffer[-1] - self.it_buffer[-2]
            )
        else:
            trend_strength = 0
            
        # Trendrichtung bestimmen
        if current_slope > 0:
            trend_direction = "aufwärts"
        elif current_slope < 0:
            trend_direction = "abwärts"
        else:
            trend_direction = "seitwärts"
            
        # Signalgenerierung
        if current_trend > current_trigger:
            signal = "long"
        elif current_trend < current_trigger:
            signal = "short"
        else:
            signal = "neutral"
            
        return {
            'trend': {
                'direction': trend_direction,
                'strength': trend_strength,
                'slope': current_slope
            },
            'signals': {
                'primary': signal,
                'trendline': current_trend,
                'trigger': current_trigger
            },
            'analysis': {
                'trend_quality': (
                    'stark' if trend_strength > 0.01
                    else 'moderat' if trend_strength > 0.005
                    else 'schwach'
                ),
                'momentum': (
                    'steigend' if current_slope > 0
                    else 'fallend' if current_slope < 0
                    else 'neutral'
                ),
                'trading_bias': (
                    'aggressiv long' if (
                        current_trend > current_trigger and
                        current_slope > 0.01
                    )
                    else 'aggressiv short' if (
                        current_trend < current_trigger and
                        current_slope < -0.01
                    )
                    else 'long' if current_trend > current_trigger
                    else 'short' if current_trend < current_trigger
                    else 'neutral'
                )
            }
        }
