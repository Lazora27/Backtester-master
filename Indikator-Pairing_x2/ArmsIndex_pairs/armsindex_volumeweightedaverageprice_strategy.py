import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VolumeWeightedAveragePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VolumeWeightedAveragePrice
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VolumeWeightedAveragePrice': 1.0
        })
    )
