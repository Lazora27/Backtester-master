import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
