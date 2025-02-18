import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
