import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'AutoFibonacci': 1.0
        })
    )
