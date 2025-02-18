import backtrader as bt

class DemandIndex(bt.Indicator):
    """
    Demand Index
    
    Ein komplexer Volumenindikator, der Angebot und Nachfrage im Markt misst.
    Kombiniert Preis und Volumen, um die Kaufkraft zu messen.
    
    Parameter:
    - price_period (13): Periode für Preisglättung
    - volume_period (13): Periode für Volumenglättung
    """
    
    lines = ('demand_index', 'signal')
    params = (
        ('price_period', 13),
        ('volume_period', 13)
    )
    
    plotlines = dict(
        demand_index=dict(color='green', _name='Demand'),
        signal=dict(color='red', _name='Signal')
    )
    
    def __init__(self):
        # Preisänderung
        price_change = self.data.close - self.data.close(-1)
        
        # Buying/Selling Pressure basierend auf Position des Schlusskurses
        high_low_range = self.data.high - self.data.low
        buying_pressure = bt.If(
            high_low_range != 0,
            (self.data.close - self.data.low) / high_low_range,
            0.5
        )
        selling_pressure = bt.If(
            high_low_range != 0,
            (self.data.high - self.data.close) / high_low_range,
            0.5
        )
        
        # Gewichtetes Volumen
        buying_volume = self.data.volume * buying_pressure
        selling_volume = self.data.volume * selling_pressure
        
        # Geglättete Komponenten
        smooth_buying = bt.indicators.EMA(buying_volume, period=self.p.volume_period)
        smooth_selling = bt.indicators.EMA(selling_volume, period=self.p.volume_period)
        smooth_price = bt.indicators.EMA(price_change, period=self.p.price_period)
        
        # Demand Index Berechnung
        self.lines.demand_index = smooth_buying - smooth_selling
        
        # Signal Line
        self.lines.signal = bt.indicators.EMA(self.lines.demand_index, period=9)
