import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
