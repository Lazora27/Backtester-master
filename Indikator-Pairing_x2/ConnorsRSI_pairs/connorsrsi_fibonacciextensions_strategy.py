import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
