import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SuperTrend
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SuperTrend': 1.0
        })
    )
