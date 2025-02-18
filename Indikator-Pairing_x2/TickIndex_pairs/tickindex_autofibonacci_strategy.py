import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
