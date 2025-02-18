import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
