import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ForecastOscillator': 1.0
        })
    )
