import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
