import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ATRTrailingStopIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ATRTrailingStopIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ATRTrailingStopIndicator': 1.0
        })
    )
