import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
