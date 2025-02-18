import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
