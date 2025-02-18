import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
