import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
