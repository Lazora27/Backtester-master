import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
