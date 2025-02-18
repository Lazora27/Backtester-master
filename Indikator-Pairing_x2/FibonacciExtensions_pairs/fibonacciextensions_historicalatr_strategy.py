import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'HistoricalATR': 1.0
        })
    )
