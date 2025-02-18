import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
