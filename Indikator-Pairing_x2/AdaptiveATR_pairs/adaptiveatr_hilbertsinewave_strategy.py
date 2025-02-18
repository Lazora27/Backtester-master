import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HilbertSinewave': 1.0
        })
    )
