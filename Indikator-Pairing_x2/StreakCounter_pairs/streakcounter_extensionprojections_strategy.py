import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ExtensionProjections': 1.0
        })
    )
