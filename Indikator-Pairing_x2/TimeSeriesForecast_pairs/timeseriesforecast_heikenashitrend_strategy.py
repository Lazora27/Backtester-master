import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
