import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'EhlersDecycler': 1.0
        })
    )
