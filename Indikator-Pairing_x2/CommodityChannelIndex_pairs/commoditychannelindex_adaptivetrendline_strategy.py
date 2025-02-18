import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
