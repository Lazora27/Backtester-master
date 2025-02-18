import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ZigZagFibonacciIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ZigZagFibonacciIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ZigZagFibonacciIndicator': 1.0
        })
    )
