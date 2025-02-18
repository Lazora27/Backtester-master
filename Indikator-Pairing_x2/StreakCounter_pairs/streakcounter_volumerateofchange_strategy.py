import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
