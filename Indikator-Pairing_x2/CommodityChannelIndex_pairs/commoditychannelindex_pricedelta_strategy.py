import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
