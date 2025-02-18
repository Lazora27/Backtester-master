import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
