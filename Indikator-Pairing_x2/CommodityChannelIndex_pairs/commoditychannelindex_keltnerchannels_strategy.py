import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
