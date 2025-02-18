import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
