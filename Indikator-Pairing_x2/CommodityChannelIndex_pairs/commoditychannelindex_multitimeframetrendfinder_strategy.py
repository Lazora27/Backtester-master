import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MultiTimeframeTrendFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MultiTimeframeTrendFinder
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MultiTimeframeTrendFinder': 1.0
        })
    )
