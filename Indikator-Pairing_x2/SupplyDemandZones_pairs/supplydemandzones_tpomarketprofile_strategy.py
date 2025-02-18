import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
