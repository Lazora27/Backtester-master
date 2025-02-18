import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'EhlersDecycler': 1.0
        })
    )
