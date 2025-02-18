import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
