import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'SeasonalStrength': 1.0
        })
    )
