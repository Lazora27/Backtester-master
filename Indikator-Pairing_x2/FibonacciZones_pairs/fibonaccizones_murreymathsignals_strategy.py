import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
