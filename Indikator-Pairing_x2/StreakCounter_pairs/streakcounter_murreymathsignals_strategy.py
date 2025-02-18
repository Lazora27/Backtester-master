import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
