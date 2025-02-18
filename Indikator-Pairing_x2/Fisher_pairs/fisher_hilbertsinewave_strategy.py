import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HilbertSinewave': 1.0
        })
    )
