import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ModifiedATR': 1.0
        })
    )
