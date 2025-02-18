import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
