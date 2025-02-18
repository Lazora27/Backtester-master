import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und VWAPBands
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'VWAPBands': 1.0
        })
    )
