import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
