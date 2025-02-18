import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'ConnorsRSI': 1.0
        })
    )
