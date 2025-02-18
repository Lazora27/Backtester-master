import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'DemandIndex': 1.0
        })
    )
