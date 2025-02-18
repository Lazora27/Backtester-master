import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
