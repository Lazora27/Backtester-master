import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TapeReading
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TapeReading': 1.0
        })
    )
