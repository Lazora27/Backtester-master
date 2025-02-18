import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
