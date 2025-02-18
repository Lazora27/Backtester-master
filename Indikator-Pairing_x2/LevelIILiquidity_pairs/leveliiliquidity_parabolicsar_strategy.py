import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'ParabolicSAR': 1.0
        })
    )
