import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'CyberCycle': 1.0
        })
    )
