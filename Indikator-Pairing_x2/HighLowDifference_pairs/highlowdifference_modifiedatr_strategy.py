import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ModifiedATR': 1.0
        })
    )
