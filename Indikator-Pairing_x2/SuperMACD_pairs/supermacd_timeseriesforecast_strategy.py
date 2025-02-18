import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
