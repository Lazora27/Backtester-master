import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'VolumeOscillator': 1.0
        })
    )
