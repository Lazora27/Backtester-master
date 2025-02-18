import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
