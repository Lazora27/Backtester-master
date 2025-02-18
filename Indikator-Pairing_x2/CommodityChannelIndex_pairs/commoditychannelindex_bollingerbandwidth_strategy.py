import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
