import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'AverageTrueRange': 1.0
        })
    )
