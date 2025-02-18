import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'HilbertSinewave': 1.0
        })
    )
