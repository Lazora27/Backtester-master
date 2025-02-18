import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DonchianVolatility': 1.0
        })
    )
