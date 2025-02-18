import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BarStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BarStrength': 1.0
        })
    )
