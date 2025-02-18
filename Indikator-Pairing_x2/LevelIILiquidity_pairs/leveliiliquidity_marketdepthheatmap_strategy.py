import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
