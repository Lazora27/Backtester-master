import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'WeeklyCycle': 1.0
        })
    )
