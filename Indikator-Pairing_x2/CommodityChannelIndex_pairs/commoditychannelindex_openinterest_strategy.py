import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
