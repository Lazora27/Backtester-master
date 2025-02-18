import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
