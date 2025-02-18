import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'WolfeWaves': 1.0
        })
    )
