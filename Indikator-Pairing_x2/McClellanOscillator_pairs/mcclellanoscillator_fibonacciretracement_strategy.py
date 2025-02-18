import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
