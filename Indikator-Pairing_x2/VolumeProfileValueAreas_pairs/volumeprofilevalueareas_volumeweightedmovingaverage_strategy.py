import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfileValueAreas_VolumeWeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfileValueAreas und VolumeWeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            },
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeProfileValueAreas': 1.0,
            'VolumeWeightedMovingAverage': 1.0
        })
    )
