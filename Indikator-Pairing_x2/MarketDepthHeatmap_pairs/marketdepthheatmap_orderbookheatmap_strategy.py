import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
