import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
