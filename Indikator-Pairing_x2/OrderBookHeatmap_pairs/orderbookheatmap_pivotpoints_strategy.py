import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PivotPoints
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PivotPoints': 1.0
        })
    )
