import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HullMovingAverage': 1.0
        })
    )
