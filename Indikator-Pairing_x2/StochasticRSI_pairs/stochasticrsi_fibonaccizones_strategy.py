import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FibonacciZones': 1.0
        })
    )
