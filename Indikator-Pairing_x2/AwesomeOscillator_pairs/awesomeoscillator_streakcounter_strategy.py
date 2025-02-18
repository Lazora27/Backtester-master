import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und StreakCounter
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'StreakCounter': 1.0
        })
    )
