import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FibonacciZones': 1.0
        })
    )
