import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
