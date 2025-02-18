import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
