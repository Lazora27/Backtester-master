import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HullMovingAverage': 1.0
        })
    )
