import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
