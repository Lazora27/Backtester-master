import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und StreakCounter
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'StreakCounter': 1.0
        })
    )
