import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
