import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
