import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'VolumeOscillator': 1.0
        })
    )
