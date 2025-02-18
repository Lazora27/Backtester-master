import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FibonacciZones': 1.0
        })
    )
