import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
