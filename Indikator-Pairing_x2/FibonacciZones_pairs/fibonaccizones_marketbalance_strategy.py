import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MarketBalance': 1.0
        })
    )
