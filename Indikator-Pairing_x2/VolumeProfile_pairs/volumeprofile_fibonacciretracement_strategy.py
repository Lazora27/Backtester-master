import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
