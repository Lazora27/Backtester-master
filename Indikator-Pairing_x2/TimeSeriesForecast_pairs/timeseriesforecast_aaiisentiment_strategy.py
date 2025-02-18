import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AAIISentiment': 1.0
        })
    )
