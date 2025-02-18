import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ZigZagFibonacciIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ZigZagFibonacciIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ZigZagFibonacciIndicator': 1.0
        })
    )
