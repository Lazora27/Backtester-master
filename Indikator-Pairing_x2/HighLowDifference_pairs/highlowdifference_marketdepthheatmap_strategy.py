import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
