import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
