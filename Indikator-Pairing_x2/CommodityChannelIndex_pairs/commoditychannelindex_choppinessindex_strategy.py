import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
