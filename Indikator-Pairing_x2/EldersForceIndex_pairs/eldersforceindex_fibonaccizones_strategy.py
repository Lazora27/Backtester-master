import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
