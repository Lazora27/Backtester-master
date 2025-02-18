import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'PhaseDivergence': 1.0
        })
    )
