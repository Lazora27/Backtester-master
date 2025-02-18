import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
