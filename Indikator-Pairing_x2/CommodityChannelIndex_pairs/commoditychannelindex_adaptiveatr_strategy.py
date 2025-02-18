import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
