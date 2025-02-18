import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BuyingPressure': 1.0
        })
    )
