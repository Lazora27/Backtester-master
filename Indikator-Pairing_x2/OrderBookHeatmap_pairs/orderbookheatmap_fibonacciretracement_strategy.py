import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
