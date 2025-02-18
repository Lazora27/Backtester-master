import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
