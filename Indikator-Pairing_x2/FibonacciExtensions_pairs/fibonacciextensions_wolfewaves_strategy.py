import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'WolfeWaves': 1.0
        })
    )
