import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TrueRange': 1.0
        })
    )
