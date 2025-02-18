import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
