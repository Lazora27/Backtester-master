import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'FibonacciZones': 1.0
        })
    )
