import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolumeWeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolumeWeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolumeWeightedMovingAverage': 1.0
        })
    )
