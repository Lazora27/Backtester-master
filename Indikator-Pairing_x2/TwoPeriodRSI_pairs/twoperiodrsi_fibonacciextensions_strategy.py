import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
