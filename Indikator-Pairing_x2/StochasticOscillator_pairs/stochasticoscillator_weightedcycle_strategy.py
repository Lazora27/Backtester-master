import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
