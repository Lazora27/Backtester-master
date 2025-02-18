import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'TrendCycles': 1.0
        })
    )
