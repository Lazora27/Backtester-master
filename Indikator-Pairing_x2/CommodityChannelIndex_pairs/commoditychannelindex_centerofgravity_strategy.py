import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
