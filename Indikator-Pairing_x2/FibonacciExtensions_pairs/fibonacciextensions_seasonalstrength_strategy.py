import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'SeasonalStrength': 1.0
        })
    )
