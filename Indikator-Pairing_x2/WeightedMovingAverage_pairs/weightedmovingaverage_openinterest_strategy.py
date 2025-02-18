import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'OpenInterest': 1.0
        })
    )
