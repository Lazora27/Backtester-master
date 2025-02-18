import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
