import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
