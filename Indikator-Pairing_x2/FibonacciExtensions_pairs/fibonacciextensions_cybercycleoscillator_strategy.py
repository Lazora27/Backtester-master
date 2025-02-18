import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
