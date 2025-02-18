import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
