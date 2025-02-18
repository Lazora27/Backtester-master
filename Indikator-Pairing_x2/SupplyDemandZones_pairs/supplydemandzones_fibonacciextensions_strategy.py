import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
