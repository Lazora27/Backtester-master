import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'CCITurbo': 1.0
        })
    )
