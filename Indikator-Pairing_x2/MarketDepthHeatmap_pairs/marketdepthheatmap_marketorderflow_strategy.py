import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
