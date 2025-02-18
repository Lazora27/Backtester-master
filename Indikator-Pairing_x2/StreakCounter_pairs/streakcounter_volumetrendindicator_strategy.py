import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
