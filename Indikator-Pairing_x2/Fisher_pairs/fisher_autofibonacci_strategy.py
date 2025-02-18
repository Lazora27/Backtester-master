import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'AutoFibonacci': 1.0
        })
    )
