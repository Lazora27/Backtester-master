import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
