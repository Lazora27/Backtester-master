import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
