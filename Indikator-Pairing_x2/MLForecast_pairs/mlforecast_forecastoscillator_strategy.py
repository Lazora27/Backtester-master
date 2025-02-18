import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ForecastOscillator': 1.0
        })
    )
