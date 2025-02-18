import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TrendExhaustion': 1.0
        })
    )
