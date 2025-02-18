import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AverageTrueRange': 1.0
        })
    )
