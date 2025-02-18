import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BradleySiderograph': 1.0
        })
    )
