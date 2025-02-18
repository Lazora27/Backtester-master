import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
