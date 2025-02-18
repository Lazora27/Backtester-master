import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StreakCounter
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StreakCounter': 1.0
        })
    )
