import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'EaseOfMovement': 1.0
        })
    )
