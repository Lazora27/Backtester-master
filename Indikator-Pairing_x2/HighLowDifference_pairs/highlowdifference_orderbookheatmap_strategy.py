import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
