import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
