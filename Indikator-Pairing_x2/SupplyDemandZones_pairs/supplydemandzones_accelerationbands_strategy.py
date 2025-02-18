import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AccelerationBands': 1.0
        })
    )
