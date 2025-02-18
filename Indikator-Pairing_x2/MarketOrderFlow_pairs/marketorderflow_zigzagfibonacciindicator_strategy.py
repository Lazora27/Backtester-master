import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ZigZagFibonacciIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ZigZagFibonacciIndicator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ZigZagFibonacciIndicator': 1.0
        })
    )
