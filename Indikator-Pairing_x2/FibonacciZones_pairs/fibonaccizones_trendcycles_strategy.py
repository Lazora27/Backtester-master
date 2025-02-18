import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TrendCycles': 1.0
        })
    )
