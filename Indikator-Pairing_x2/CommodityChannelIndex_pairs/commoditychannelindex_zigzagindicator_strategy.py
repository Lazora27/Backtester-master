import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
