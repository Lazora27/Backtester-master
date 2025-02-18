import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FibonacciZones': 1.0
        })
    )
