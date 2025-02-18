import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
