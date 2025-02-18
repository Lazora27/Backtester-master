import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'Fisher': 1.0
        })
    )
