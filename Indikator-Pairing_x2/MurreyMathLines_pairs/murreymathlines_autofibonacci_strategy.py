import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AutoFibonacci': 1.0
        })
    )
