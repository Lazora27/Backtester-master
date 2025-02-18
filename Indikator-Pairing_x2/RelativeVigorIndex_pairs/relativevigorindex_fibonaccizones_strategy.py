import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
