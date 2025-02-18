import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
