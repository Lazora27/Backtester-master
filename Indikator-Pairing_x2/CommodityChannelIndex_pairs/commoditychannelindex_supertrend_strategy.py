import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
