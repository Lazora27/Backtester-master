import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
