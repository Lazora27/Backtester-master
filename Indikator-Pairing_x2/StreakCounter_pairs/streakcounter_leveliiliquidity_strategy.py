import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
