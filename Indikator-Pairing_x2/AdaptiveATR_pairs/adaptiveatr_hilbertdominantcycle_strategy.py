import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
