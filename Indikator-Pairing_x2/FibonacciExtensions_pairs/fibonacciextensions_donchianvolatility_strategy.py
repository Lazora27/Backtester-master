import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'DonchianVolatility': 1.0
        })
    )
