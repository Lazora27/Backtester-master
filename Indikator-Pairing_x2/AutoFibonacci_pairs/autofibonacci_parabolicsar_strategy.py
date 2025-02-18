import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ParabolicSAR': 1.0
        })
    )
