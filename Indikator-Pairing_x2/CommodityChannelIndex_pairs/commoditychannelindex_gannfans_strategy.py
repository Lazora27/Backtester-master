import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'GannFans': 1.0
        })
    )
