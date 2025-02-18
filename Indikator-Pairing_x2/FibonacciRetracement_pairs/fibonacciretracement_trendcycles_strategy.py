import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'TrendCycles': 1.0
        })
    )
