import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
