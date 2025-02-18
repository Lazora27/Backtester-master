import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_VolumeWeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und VolumeWeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'VolumeWeightedMovingAverage': 1.0
        })
    )
