import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
