import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
