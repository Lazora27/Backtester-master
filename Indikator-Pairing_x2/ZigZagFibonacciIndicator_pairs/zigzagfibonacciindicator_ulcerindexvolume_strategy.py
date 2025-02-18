import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagFibonacciIndicator_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagFibonacciIndicator und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ZigZagFibonacciIndicator': {
                'class': ZigZagFibonacciIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagFibonacciIndicator'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ZigZagFibonacciIndicator': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
