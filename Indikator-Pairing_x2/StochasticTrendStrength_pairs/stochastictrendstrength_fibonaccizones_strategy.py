import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FibonacciZones': 1.0
        })
    )
