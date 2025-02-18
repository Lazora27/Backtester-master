import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
