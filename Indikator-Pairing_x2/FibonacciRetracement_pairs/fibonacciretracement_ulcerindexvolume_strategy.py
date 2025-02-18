import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
