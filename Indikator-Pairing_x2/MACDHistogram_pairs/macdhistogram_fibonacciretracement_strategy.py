import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
