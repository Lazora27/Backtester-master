import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
