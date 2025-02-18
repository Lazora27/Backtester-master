import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
