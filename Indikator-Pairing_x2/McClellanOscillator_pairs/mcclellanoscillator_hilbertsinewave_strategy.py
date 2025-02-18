import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
