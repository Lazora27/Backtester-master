import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
