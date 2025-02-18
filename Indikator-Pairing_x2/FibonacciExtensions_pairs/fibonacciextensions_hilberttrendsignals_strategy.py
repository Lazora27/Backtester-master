import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
