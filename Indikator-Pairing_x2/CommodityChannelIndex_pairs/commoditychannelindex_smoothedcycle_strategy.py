import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
