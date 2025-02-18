import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'VolumeDelta': 1.0
        })
    )
