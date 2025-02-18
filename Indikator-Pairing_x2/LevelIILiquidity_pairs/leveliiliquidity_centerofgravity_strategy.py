import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'CenterOfGravity': 1.0
        })
    )
