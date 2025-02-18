import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AutoFibonacci': 1.0
        })
    )
