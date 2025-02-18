import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
