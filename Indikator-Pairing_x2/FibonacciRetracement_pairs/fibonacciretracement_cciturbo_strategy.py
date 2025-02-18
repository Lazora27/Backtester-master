import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'CCITurbo': 1.0
        })
    )
