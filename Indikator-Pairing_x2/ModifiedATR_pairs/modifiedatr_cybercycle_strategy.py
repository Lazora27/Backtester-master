import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'CyberCycle': 1.0
        })
    )
