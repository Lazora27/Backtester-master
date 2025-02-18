import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und StreakCounter
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'StreakCounter': 1.0
        })
    )
