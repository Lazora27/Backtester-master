import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
