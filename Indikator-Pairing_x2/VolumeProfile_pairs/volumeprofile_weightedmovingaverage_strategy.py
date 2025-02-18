import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
