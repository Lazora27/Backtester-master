import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
