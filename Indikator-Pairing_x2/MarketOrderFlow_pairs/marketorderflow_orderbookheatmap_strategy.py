import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
