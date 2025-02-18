import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
