import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'WolfeWaves': 1.0
        })
    )
