import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'WeeklyCycle': 1.0
        })
    )
