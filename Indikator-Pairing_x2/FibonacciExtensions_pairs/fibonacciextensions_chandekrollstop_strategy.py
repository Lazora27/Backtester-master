import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
