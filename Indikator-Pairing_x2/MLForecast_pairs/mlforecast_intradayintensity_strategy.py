import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'IntradayIntensity': 1.0
        })
    )
