import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
