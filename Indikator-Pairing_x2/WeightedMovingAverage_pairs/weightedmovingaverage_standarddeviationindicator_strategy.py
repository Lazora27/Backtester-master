import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
