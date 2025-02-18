import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
