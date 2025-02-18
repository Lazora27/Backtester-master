import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und GannFans
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'GannFans': 1.0
        })
    )
