import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'IntradayIntensity': 1.0
        })
    )
