import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
