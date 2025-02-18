import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
