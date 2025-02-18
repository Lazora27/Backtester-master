import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MurreyMathLines': 1.0
        })
    )
