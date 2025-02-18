import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
