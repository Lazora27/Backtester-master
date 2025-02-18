import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
