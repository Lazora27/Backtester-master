import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
