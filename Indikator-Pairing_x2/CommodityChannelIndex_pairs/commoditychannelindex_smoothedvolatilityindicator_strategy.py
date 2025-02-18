import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SmoothedVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SmoothedVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SmoothedVolatilityIndicator': 1.0
        })
    )
