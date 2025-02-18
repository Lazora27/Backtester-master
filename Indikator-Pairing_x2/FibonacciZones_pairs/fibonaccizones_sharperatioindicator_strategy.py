import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
