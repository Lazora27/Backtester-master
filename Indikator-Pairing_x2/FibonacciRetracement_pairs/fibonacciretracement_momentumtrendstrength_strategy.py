import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
