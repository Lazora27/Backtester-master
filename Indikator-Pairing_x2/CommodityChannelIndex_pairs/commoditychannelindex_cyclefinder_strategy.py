import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
