import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CumulativeTick': 1.0
        })
    )
