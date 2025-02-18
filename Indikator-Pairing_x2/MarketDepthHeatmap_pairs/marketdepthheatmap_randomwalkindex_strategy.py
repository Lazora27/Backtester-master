import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
