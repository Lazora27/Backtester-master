import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HilbertSinewave': 1.0
        })
    )
