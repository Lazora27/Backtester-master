import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und CCITurbo
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'CCITurbo': 1.0
        })
    )
