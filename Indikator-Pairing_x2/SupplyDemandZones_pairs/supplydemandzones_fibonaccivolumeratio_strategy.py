import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FibonacciVolumeRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FibonacciVolumeRatio
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FibonacciVolumeRatio': {
                'class': FibonacciVolumeRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciVolumeRatio'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FibonacciVolumeRatio': 1.0
        })
    )
