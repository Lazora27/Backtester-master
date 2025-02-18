import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
