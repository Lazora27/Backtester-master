import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SmoothedCycle': 1.0
        })
    )
