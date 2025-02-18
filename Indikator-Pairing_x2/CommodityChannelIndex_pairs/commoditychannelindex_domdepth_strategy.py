import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
