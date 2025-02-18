import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
