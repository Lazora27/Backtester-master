import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
