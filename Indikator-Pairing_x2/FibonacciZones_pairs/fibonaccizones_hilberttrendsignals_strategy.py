import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
