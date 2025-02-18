import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
