import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
