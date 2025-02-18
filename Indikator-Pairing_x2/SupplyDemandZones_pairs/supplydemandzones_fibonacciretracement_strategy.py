import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
