import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
