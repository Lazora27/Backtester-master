import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
