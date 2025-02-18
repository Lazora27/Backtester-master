import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
