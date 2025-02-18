import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CommodityChannelIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CommodityChannelIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CommodityChannelIndex': 1.0
        })
    )
