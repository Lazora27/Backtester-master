import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'StochasticOscillator': 1.0
        })
    )
