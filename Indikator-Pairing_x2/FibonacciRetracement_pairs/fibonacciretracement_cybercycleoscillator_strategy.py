import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
