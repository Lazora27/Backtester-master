import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'FibonacciZones': 1.0
        })
    )
