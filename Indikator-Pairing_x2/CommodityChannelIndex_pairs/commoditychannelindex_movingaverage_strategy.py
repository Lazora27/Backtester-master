import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CommodityChannelIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CommodityChannelIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'CommodityChannelIndex': {
                'class': CommodityChannelIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CommodityChannelIndex1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'CommodityChannelIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
