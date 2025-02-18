import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
