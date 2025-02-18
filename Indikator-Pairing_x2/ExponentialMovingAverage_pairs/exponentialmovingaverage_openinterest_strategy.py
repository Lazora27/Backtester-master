import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'OpenInterest': 1.0
        })
    )
