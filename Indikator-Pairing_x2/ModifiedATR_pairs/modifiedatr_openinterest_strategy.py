import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'OpenInterest': 1.0
        })
    )
