import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
