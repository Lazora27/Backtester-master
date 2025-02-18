import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AAIISentiment': 1.0
        })
    )
