import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'TimeCycle': 1.0
        })
    )
