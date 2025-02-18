import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
