import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_VolumeWeightedAveragePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und VolumeWeightedAveragePrice
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'VolumeWeightedAveragePrice': 1.0
        })
    )
