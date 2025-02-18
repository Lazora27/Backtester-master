import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
