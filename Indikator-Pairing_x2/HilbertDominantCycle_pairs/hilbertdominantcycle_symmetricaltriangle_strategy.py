import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
