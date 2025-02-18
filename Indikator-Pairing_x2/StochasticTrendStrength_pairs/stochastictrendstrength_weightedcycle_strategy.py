import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WeightedCycle': 1.0
        })
    )
