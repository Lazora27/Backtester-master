import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HilbertSinewave': 1.0
        })
    )
