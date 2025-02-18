import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'WeightedCycle': 1.0
        })
    )
