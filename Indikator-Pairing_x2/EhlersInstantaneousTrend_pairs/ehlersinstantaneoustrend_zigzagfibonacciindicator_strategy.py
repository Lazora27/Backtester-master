import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrend_ZigZagFibonacciIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrend und ZigZagFibonacciIndicator
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            },
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrend': 1.0,
            'ZigZagFibonacciIndicator': 1.0
        })
    )
