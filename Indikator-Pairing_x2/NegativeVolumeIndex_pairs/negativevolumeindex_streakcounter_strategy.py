import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
