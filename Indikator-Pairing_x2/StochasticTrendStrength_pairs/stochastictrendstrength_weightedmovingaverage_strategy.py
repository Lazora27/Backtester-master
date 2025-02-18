import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
