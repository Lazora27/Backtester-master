import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
