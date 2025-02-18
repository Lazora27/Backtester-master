import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagFibonacciIndicator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagFibonacciIndicator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ZigZagFibonacciIndicator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
