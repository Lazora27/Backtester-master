import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
