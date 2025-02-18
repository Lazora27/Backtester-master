import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
