import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
