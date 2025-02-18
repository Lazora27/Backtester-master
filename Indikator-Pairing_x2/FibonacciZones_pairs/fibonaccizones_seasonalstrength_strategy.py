import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'SeasonalStrength': 1.0
        })
    )
