import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DemandIndex': 1.0
        })
    )
