import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
