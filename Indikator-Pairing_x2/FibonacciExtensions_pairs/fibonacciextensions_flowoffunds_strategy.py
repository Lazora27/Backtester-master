import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'FlowOfFunds': 1.0
        })
    )
