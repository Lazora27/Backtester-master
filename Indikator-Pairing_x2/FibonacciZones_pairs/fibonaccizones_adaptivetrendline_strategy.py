import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
