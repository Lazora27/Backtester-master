import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
