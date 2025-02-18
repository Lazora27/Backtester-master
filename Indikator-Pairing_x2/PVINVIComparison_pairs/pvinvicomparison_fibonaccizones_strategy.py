import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'FibonacciZones': 1.0
        })
    )
