import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BuyingPressure': 1.0
        })
    )
