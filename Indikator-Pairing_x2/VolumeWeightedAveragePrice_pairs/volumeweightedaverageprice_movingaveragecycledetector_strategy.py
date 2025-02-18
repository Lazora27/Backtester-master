import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedAveragePrice_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedAveragePrice und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'VolumeWeightedAveragePrice': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
