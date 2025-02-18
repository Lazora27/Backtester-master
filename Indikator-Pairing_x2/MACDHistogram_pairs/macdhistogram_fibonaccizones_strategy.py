import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FibonacciZones': 1.0
        })
    )
