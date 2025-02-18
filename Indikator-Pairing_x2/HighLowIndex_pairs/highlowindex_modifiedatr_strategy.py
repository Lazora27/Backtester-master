import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ModifiedATR': 1.0
        })
    )
