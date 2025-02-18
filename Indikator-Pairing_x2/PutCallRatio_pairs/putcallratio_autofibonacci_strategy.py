import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AutoFibonacci': 1.0
        })
    )
