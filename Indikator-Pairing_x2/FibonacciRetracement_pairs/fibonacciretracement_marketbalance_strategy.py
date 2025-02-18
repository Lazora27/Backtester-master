import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'MarketBalance': 1.0
        })
    )
