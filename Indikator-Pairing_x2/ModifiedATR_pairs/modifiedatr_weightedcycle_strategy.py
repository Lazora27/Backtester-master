import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'WeightedCycle': 1.0
        })
    )
