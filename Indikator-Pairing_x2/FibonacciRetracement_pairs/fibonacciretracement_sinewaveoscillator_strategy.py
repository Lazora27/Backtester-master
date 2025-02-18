import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
