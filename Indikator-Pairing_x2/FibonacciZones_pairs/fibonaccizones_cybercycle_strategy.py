import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'CyberCycle': 1.0
        })
    )
