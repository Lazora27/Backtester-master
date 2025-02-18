import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TapeReading
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TapeReading': 1.0
        })
    )
