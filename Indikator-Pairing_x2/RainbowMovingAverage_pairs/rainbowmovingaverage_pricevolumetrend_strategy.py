import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
