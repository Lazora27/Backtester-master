import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
