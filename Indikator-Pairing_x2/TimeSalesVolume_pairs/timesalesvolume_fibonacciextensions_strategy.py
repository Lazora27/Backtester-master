import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
