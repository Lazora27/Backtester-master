import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MarketBalance': 1.0
        })
    )
