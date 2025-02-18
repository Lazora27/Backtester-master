import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
