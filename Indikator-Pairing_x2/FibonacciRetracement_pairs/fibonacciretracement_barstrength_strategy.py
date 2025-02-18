import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BarStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BarStrength': 1.0
        })
    )
