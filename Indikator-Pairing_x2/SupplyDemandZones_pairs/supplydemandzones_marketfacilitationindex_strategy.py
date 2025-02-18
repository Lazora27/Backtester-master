import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
