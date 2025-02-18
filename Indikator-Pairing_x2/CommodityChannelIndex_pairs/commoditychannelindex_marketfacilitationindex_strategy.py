import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
