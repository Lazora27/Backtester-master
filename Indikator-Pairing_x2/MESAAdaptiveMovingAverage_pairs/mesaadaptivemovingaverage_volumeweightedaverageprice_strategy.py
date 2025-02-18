import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MESAAdaptiveMovingAverage_VolumeWeightedAveragePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MESAAdaptiveMovingAverage und VolumeWeightedAveragePrice
    """
    
    params = (
        ('indicators', {
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            },
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            }
        }),
        ('weights', {
            'MESAAdaptiveMovingAverage': 1.0,
            'VolumeWeightedAveragePrice': 1.0
        })
    )
