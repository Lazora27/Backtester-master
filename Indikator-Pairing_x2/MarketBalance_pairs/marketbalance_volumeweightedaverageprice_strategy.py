import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_VolumeWeightedAveragePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und VolumeWeightedAveragePrice
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'VolumeWeightedAveragePrice': 1.0
        })
    )
