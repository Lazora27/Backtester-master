import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
