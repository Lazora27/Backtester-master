import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'IntradayIntensity': 1.0
        })
    )
