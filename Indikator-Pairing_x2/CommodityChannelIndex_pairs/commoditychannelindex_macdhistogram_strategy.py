import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
