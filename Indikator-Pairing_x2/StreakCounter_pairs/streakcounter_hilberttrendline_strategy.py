import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HilbertTrendline': 1.0
        })
    )
