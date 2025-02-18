import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'SmoothedCycle': 1.0
        })
    )
