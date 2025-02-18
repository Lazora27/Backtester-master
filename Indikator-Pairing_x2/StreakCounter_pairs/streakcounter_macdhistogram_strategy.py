import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MACDHistogram': 1.0
        })
    )
