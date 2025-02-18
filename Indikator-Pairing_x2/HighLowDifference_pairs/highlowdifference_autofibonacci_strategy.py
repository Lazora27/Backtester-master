import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AutoFibonacci': 1.0
        })
    )
