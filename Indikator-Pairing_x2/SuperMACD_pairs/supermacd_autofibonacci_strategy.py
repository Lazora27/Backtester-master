import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AutoFibonacci': 1.0
        })
    )
