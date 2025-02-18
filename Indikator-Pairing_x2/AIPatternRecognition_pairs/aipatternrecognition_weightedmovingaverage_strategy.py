import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
