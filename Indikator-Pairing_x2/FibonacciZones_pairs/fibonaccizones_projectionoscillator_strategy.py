import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
