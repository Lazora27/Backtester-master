import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeProfile': 1.0
        })
    )
