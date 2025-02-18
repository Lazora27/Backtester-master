import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BradleySiderograph': 1.0
        })
    )
