import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AAIISentiment': 1.0
        })
    )
