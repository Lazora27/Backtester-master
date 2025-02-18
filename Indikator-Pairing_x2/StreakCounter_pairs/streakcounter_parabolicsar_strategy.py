import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ParabolicSAR': 1.0
        })
    )
