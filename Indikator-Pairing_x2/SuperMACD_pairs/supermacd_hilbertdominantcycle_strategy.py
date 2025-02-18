import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
