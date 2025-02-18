import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
