import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'OpenInterest': 1.0
        })
    )
