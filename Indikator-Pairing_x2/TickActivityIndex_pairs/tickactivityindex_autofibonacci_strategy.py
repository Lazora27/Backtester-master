import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
