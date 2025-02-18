import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
