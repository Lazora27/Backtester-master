import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HilbertSinewave': 1.0
        })
    )
