import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
