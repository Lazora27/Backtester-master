import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'IchimokuCloud': 1.0
        })
    )
