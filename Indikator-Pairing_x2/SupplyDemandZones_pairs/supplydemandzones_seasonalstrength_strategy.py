import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SeasonalStrength': 1.0
        })
    )
