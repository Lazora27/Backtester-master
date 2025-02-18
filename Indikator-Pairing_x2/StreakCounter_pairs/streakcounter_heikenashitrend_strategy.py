import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
