import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
