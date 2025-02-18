import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
