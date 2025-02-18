import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_VolumeWeightedAveragePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und VolumeWeightedAveragePrice
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'VolumeWeightedAveragePrice': 1.0
        })
    )
