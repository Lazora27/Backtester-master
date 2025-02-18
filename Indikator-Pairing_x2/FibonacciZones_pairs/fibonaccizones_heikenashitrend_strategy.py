import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
