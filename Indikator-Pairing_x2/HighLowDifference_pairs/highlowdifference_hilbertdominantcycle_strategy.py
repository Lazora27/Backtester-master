import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
