import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
