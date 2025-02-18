import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AccelerationBands': 1.0
        })
    )
