import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HilbertSinewave': 1.0
        })
    )
