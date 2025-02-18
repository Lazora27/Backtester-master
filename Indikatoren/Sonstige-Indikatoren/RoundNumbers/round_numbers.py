import backtrader as bt
import numpy as np

class RoundNumbersIndicator(bt.Indicator):
    """
    Round Numbers Indicator
    
    Ein Indikator zur Identifizierung und Analyse von
    psychologisch wichtigen runden Zahlen.
    
    Features:
    - Erkennung runder Zahlen
    - Unterstützungs-/Widerstandszonen
    - Preismagnet-Analyse
    - Clustering-Erkennung
    
    Parameter:
    - levels (10): Anzahl der Levels
    - zone_size (0.1): Zonengröße in %
    """
    
    lines = ('support', 'resistance', 'magnet_strength')
    params = (
        ('levels', 10),
        ('zone_size', 0.1),
    )
    
    plotlines = dict(
        support=dict(color='green', _name='Support'),
        resistance=dict(color='red', _name='Resistance'),
        magnet_strength=dict(color='blue', _name='Magnet Strength')
    )
    
    def __init__(self):
        super(RoundNumbersIndicator, self).__init__()
        
        # Preispuffer
        self.price_history = []
        
        # Runde Zahlen Cache
        self.round_numbers = set()
        
        # Zone-Cache
        self.support_zones = []
        self.resistance_zones = []
        
    def find_round_numbers(self, price):
        """Findet runde Zahlen um den Preis"""
        # Dezimalstellen bestimmen
        magnitude = len(str(int(price)))
        round_numbers = set()
        
        # Verschiedene Rundungsstufen
        for i in range(magnitude):
            base = 10 ** i
            
            # Auf- und Abrunden
            rounded_up = np.ceil(price / base) * base
            rounded_down = np.floor(price / base) * base
            
            # Zwischenwerte
            mid_up = (rounded_up + price) / 2
            mid_down = (rounded_down + price) / 2
            
            round_numbers.update([
                rounded_up,
                rounded_down,
                mid_up,
                mid_down
            ])
            
        return round_numbers
        
    def calculate_magnet_strength(self, price, round_number):
        """Berechnet die Magnetstärke einer runden Zahl"""
        distance = abs(price - round_number)
        if distance == 0:
            return 1.0
            
        # Abstandsbasierte Stärke
        strength = 1.0 / (1.0 + distance)
        
        # Historische Preisreaktionen
        if self.price_history:
            reactions = 0
            total = 0
            
            for hist_price in self.price_history[-100:]:
                if abs(hist_price - round_number) < (
                    self.p.zone_size * round_number
                ):
                    reactions += 1
                total += 1
                
            if total > 0:
                reaction_factor = reactions / total
                strength *= (1 + reaction_factor)
                
        return min(1.0, strength)
        
    def identify_zones(self, price):
        """Identifiziert S/R-Zonen"""
        zones = []
        
        for number in self.round_numbers:
            zone_size = number * self.p.zone_size
            
            # Zone definieren
            zone = {
                'center': number,
                'upper': number + zone_size,
                'lower': number - zone_size,
                'strength': self.calculate_magnet_strength(
                    price,
                    number
                )
            }
            
            zones.append(zone)
            
        # Nach Stärke sortieren
        zones.sort(key=lambda x: x['strength'], reverse=True)
        
        # Auf wichtigste Zonen beschränken
        return zones[:self.p.levels]
        
    def next(self):
        price = self.data.close[0]
        
        # Preishistorie aktualisieren
        self.price_history.append(price)
        if len(self.price_history) > 1000:  # Limit Historie
            self.price_history.pop(0)
            
        # Runde Zahlen aktualisieren
        self.round_numbers = self.find_round_numbers(price)
        
        # Zonen identifizieren
        zones = self.identify_zones(price)
        
        # Support/Resistance bestimmen
        support_level = 0
        resistance_level = 0
        max_magnet = 0
        
        for zone in zones:
            if zone['center'] < price:
                if zone['strength'] > support_level:
                    support_level = zone['center']
            else:
                if zone['strength'] > resistance_level:
                    resistance_level = zone['center']
                    
            # Stärkster Magnet
            if zone['strength'] > max_magnet:
                max_magnet = zone['strength']
                
        # Linien aktualisieren
        self.lines.support[0] = support_level
        self.lines.resistance[0] = resistance_level
        self.lines.magnet_strength[0] = max_magnet
        
    def get_analysis(self):
        """
        Liefert eine detaillierte Analyse des Indikators.
        """
        price = self.data.close[0]
        
        # Aktive Zonen
        zones = self.identify_zones(price)
        
        # Nächste wichtige Levels
        next_support = None
        next_resistance = None
        
        for zone in zones:
            if zone['center'] < price:
                if (next_support is None or
                    zone['center'] > next_support['center']):
                    next_support = zone
            else:
                if (next_resistance is None or
                    zone['center'] < next_resistance['center']):
                    next_resistance = zone
                    
        return {
            'price_analysis': {
                'current_price': price,
                'nearest_round': min(
                    self.round_numbers,
                    key=lambda x: abs(x - price)
                ),
                'magnet_strength': self.lines.magnet_strength[0]
            },
            'support_resistance': {
                'support': {
                    'level': (
                        next_support['center']
                        if next_support else None
                    ),
                    'strength': (
                        next_support['strength']
                        if next_support else 0
                    ),
                    'zone': (
                        [next_support['lower'],
                         next_support['upper']]
                        if next_support else None
                    )
                },
                'resistance': {
                    'level': (
                        next_resistance['center']
                        if next_resistance else None
                    ),
                    'strength': (
                        next_resistance['strength']
                        if next_resistance else 0
                    ),
                    'zone': (
                        [next_resistance['lower'],
                         next_resistance['upper']]
                        if next_resistance else None
                    )
                }
            },
            'trading_zones': {
                'active_zones': [
                    {
                        'level': zone['center'],
                        'strength': zone['strength'],
                        'type': (
                            'support'
                            if zone['center'] < price
                            else 'resistance'
                        )
                    }
                    for zone in zones
                ],
                'clustering': len([
                    z for z in zones
                    if abs(z['center'] - price) <
                    price * self.p.zone_size
                ])
            },
            'market_context': {
                'price_magnetism': (
                    'stark' if self.lines.magnet_strength[0] > 0.7
                    else 'moderat'
                    if self.lines.magnet_strength[0] > 0.3
                    else 'schwach'
                ),
                'zone_density': len(zones) / self.p.levels,
                'price_position': (
                    'zwischen_zonen'
                    if not any(
                        abs(z['center'] - price) <
                        price * self.p.zone_size
                        for z in zones
                    )
                    else 'in_zone'
                )
            }
        }
