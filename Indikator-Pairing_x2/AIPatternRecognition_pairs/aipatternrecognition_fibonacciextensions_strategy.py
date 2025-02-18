import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
