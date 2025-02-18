import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
