import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AutoFibonacci': 1.0
        })
    )
