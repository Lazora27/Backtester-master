import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
