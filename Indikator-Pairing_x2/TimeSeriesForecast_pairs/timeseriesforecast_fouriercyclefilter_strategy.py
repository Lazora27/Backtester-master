import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
