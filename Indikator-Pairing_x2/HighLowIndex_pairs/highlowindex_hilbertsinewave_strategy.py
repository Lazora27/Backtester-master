import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
