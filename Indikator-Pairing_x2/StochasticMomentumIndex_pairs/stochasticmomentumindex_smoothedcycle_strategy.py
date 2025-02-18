import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
