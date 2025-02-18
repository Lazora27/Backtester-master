import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
