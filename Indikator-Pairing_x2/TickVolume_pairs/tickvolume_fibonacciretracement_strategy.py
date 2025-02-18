import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
