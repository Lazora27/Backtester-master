import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
