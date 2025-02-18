import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und GannFans
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'GannFans': 1.0
        })
    )
