import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HilbertSinewave': 1.0
        })
    )
