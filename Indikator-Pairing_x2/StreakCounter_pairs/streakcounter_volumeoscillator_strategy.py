import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeOscillator': 1.0
        })
    )
