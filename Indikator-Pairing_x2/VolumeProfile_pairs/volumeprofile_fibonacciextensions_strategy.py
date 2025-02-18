import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
