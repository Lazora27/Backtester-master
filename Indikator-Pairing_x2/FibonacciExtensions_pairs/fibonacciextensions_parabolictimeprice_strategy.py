import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
