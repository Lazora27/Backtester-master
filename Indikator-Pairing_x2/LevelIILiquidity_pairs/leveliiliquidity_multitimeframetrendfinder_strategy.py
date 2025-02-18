import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_MultiTimeframeTrendFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und MultiTimeframeTrendFinder
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'MultiTimeframeTrendFinder': 1.0
        })
    )
