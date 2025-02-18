import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
