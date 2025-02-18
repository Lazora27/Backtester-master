import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
