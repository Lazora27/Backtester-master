import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
