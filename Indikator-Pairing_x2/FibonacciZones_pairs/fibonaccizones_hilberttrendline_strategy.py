import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HilbertTrendline': 1.0
        })
    )
