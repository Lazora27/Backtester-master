import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und CycleFinder
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'CycleFinder': 1.0
        })
    )
