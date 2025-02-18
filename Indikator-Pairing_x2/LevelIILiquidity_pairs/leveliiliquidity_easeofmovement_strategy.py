import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'EaseOfMovement': 1.0
        })
    )
