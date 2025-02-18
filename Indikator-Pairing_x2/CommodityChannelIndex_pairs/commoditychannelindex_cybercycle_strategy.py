import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
