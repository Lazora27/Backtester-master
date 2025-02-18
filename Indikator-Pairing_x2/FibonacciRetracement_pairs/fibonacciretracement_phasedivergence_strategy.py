import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'PhaseDivergence': 1.0
        })
    )
