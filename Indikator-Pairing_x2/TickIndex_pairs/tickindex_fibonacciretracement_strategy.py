import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
