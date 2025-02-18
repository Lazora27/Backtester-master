import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'UlcerIndex': 1.0
        })
    )
