import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HilbertTrendline': 1.0
        })
    )
