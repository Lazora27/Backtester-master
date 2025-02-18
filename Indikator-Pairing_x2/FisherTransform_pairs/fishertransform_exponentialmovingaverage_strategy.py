import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
