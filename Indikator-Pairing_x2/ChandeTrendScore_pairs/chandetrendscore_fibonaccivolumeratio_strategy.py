import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FibonacciVolumeRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FibonacciVolumeRatio
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FibonacciVolumeRatio': 1.0
        })
    )
