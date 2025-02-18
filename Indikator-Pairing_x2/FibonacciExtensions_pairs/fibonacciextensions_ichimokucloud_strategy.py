import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'IchimokuCloud': 1.0
        })
    )
