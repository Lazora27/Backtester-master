import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
