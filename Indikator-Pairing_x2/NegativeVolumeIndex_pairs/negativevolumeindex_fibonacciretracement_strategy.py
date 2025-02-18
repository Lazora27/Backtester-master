import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
