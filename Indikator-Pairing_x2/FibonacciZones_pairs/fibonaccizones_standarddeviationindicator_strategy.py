import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
