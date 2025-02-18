import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
