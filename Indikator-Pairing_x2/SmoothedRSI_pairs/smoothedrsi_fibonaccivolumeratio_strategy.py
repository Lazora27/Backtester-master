import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FibonacciVolumeRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FibonacciVolumeRatio
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FibonacciVolumeRatio': 1.0
        })
    )
