import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und StreakCounter
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'StreakCounter': 1.0
        })
    )
