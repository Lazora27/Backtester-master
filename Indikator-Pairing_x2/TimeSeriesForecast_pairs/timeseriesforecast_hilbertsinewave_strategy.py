import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HilbertSinewave': 1.0
        })
    )
