import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'HilbertSinewave': 1.0
        })
    )
