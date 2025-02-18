import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
