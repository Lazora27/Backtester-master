import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ParabolicSAR': 1.0
        })
    )
