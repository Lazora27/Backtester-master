import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HilbertSinewave': 1.0
        })
    )
