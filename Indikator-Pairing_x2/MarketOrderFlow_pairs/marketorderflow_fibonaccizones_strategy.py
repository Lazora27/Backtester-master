import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FibonacciZones': 1.0
        })
    )
