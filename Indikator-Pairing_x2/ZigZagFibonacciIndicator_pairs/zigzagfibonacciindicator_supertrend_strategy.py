import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagFibonacciIndicator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagFibonacciIndicator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ZigZagFibonacciIndicator': 1.0,
            'SuperTrend': 1.0
        })
    )
