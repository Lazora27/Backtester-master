import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HilbertSinewave': 1.0
        })
    )
