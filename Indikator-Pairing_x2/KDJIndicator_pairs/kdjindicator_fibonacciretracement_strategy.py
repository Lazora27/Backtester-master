import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
