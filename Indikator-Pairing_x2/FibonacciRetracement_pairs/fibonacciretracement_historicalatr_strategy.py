import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HistoricalATR': 1.0
        })
    )
