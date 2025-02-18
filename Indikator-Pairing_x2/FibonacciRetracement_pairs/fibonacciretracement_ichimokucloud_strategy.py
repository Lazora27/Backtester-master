import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'IchimokuCloud': 1.0
        })
    )
