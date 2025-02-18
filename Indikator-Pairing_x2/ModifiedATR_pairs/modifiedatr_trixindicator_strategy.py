import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'TRIXIndicator': 1.0
        })
    )
