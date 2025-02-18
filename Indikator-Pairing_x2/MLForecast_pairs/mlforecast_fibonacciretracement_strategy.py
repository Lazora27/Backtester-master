import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
