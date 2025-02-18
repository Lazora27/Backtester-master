import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
