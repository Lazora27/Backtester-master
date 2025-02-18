import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
