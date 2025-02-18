import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'GannAngles': 1.0
        })
    )
