import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
