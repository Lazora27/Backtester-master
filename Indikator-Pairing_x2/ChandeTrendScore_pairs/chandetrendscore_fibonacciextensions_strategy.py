import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
