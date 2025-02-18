import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HilbertSinewave': 1.0
        })
    )
