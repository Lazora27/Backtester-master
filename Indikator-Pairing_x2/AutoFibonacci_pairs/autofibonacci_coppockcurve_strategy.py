import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CoppockCurve': 1.0
        })
    )
