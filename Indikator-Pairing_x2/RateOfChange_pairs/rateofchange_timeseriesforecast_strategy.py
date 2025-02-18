import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
