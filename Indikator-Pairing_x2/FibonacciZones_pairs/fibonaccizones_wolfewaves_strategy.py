import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'WolfeWaves': 1.0
        })
    )
