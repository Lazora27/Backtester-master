import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'EaseOfMovement': 1.0
        })
    )
