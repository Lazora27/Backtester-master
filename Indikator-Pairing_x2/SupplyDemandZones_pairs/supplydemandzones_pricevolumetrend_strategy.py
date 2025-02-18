import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
