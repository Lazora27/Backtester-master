import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AverageTrueRange': 1.0
        })
    )
