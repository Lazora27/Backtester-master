import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FibonacciZones': 1.0
        })
    )
