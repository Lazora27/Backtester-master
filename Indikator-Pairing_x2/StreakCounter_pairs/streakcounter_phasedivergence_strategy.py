import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'PhaseDivergence': 1.0
        })
    )
