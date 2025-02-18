import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
