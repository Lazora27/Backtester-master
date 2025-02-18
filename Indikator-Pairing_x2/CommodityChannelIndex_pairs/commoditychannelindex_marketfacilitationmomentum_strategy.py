import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MarketFacilitationMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MarketFacilitationMomentum
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MarketFacilitationMomentum': 1.0
        })
    )
