import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
