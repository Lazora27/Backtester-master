import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'PivotPoints': 1.0
        })
    )
