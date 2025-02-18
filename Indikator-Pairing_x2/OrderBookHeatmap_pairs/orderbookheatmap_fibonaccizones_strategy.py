import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FibonacciZones': 1.0
        })
    )
