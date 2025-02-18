import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
