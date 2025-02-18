import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsEaseOfMovement_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsEaseOfMovement und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ArmsEaseOfMovement': 1.0,
            'HilbertSinewave': 1.0
        })
    )
