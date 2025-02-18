import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ModifiedATR': 1.0
        })
    )
