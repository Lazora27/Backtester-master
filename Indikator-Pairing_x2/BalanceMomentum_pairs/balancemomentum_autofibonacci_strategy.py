import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AutoFibonacci': 1.0
        })
    )
