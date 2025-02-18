import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und StreakCounter
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'StreakCounter': 1.0
        })
    )
