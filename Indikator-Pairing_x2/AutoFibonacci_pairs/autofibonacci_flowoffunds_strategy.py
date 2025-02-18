import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'FlowOfFunds': 1.0
        })
    )
