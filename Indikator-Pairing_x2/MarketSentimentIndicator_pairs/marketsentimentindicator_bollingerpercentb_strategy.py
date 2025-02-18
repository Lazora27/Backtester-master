import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
