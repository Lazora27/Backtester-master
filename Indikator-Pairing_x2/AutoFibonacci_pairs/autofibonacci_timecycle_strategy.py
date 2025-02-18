import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'TimeCycle': 1.0
        })
    )
