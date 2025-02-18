import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
