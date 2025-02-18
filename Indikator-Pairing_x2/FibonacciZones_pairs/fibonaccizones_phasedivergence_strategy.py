import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PhaseDivergence': 1.0
        })
    )
