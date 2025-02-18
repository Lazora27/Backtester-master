import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
