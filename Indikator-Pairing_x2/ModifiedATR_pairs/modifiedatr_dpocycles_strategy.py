import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'DPOCycles': 1.0
        })
    )
