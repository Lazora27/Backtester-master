import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
