import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
