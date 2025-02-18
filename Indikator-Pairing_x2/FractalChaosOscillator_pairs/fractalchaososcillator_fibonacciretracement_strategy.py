import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
