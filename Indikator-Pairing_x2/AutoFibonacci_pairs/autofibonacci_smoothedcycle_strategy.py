import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SmoothedCycle': 1.0
        })
    )
