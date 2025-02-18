import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und MassIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'MassIndex': 1.0
        })
    )
