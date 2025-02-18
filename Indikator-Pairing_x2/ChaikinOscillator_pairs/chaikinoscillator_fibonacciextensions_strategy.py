import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
