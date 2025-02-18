import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'DonchianVolatility': 1.0
        })
    )
