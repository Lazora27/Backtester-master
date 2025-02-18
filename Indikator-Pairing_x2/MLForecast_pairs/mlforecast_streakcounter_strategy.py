import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und StreakCounter
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'StreakCounter': 1.0
        })
    )
