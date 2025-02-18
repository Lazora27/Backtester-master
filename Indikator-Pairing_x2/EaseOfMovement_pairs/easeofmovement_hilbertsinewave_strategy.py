import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'HilbertSinewave': 1.0
        })
    )
