import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HilbertSinewave': 1.0
        })
    )
