import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AverageLogRange': 1.0
        })
    )
