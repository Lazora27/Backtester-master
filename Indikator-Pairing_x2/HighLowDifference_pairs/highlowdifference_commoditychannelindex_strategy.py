import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
