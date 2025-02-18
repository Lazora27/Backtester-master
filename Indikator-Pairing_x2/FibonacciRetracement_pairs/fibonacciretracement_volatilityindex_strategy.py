import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'VolatilityIndex': 1.0
        })
    )
