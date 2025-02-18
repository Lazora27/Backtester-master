import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'HilbertSinewave': 1.0
        })
    )
