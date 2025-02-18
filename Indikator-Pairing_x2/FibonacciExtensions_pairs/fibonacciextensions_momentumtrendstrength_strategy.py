import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
