import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und MassIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'MassIndex': 1.0
        })
    )
