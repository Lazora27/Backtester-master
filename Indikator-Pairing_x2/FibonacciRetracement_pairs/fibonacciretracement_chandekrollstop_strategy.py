import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
