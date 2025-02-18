import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
