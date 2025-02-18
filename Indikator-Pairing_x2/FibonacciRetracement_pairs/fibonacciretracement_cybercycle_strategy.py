import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und CyberCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'CyberCycle': 1.0
        })
    )
