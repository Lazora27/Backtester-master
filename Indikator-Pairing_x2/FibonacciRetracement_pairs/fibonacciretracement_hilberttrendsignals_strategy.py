import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
