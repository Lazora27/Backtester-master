import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
