import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
