import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
