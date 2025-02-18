import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MovingAverage': 1.0
        })
    )
