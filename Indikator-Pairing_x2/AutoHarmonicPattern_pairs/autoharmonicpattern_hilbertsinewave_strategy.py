import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'HilbertSinewave': 1.0
        })
    )
