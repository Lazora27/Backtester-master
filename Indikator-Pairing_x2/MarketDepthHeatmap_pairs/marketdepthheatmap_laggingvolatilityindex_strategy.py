import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
