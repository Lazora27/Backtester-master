import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'VortexIndicator': 1.0
        })
    )
