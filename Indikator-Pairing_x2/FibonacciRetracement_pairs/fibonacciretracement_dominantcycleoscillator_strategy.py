import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
