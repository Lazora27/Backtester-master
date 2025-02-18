import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AAIISentiment': 1.0
        })
    )
