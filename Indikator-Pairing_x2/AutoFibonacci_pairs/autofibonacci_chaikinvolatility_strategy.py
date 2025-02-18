import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
