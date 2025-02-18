import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedMovingAverage_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedMovingAverage und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'VolumeWeightedMovingAverage': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
