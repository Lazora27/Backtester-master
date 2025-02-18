import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SuperTrend': 1.0
        })
    )
