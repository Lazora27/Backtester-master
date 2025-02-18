import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
