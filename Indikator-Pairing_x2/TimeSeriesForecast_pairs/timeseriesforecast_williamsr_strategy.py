import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'WilliamsR': 1.0
        })
    )
