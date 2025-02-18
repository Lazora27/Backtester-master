import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'CenterOfGravity': 1.0
        })
    )
