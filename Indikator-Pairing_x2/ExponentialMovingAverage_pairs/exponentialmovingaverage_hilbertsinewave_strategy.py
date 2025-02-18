import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'HilbertSinewave': 1.0
        })
    )
