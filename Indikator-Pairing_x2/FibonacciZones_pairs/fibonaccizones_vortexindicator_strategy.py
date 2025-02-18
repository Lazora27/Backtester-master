import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VortexIndicator': 1.0
        })
    )
