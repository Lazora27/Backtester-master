import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'WeeklyCycle': 1.0
        })
    )
