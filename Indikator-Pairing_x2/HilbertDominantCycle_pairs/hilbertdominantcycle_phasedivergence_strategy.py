import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'PhaseDivergence': 1.0
        })
    )
