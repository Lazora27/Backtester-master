import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
