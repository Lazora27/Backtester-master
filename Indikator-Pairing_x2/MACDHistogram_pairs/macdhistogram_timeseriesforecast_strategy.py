import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
