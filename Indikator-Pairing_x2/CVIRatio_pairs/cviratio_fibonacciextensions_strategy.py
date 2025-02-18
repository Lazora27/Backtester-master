import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
