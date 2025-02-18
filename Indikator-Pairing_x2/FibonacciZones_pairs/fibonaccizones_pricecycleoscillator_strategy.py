import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
