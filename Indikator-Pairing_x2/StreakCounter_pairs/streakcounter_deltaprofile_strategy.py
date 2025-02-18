import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DeltaProfile': 1.0
        })
    )
