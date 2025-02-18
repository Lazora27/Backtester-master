import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AutoFibonacci': 1.0
        })
    )
