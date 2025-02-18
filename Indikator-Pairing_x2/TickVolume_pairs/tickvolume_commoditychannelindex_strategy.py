import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
