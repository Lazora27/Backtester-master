import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
