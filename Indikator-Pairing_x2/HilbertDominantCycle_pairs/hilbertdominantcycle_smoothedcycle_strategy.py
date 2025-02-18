import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'SmoothedCycle': 1.0
        })
    )
