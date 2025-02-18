import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
