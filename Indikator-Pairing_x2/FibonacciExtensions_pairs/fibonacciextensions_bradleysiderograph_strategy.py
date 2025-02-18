import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BradleySiderograph': 1.0
        })
    )
