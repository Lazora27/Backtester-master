import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'ModifiedATR': 1.0
        })
    )
