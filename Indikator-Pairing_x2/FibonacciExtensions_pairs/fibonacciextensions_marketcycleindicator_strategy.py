import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
