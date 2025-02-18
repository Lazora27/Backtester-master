import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
