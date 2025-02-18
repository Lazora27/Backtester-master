import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'FibonacciZones': 1.0
        })
    )
