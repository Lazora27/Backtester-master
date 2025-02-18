import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
