import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
