import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
