import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'OpenInterest': 1.0
        })
    )
