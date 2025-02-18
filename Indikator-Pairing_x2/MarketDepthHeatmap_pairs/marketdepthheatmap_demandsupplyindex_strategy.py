import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
