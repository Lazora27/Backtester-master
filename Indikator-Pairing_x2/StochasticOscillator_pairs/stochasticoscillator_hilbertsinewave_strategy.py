import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
