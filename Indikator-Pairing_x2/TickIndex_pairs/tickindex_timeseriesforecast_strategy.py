import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
