import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'SmoothedCycle': 1.0
        })
    )
