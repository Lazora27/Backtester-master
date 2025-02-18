import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
