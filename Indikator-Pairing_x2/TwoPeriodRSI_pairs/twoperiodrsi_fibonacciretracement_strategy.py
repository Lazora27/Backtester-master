import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
