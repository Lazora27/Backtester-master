import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TickActivityIndex': 1.0
        })
    )
