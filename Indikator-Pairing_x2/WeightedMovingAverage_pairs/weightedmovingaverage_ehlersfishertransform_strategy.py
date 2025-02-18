import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
