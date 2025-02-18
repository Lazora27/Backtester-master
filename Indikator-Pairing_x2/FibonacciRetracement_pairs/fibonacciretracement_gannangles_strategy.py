import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und GannAngles
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'GannAngles': 1.0
        })
    )
