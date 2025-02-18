import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
