import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
