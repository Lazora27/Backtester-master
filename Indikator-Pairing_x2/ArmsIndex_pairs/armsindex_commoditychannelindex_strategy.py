import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
