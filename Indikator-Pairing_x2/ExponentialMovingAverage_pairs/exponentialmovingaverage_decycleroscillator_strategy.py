import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
