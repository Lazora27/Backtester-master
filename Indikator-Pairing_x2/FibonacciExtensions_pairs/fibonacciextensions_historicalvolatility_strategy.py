import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
