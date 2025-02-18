import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
