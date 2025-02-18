import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
