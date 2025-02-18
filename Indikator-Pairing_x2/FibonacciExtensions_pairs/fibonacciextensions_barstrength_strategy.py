import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BarStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BarStrength': 1.0
        })
    )
