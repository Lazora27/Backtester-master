import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
