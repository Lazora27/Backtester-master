import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
