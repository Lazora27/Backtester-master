import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
