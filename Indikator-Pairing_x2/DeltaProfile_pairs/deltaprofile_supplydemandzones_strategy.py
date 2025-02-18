import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
