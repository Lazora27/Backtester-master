import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AverageLogRange': 1.0
        })
    )
