import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
