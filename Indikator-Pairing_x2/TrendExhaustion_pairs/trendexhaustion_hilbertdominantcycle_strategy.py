import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
