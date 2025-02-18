import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'FisherSignals': 1.0
        })
    )
