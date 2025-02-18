import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'MarketBalance': 1.0
        })
    )
