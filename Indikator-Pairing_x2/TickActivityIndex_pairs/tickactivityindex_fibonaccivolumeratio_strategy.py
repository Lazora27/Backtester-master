import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FibonacciVolumeRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FibonacciVolumeRatio
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FibonacciVolumeRatio': 1.0
        })
    )
