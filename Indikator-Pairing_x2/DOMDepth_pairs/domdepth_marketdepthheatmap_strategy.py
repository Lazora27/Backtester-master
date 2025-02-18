import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
