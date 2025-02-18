import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'WeeklyCycle': 1.0
        })
    )
