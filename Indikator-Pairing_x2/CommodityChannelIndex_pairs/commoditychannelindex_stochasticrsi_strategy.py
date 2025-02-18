import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
