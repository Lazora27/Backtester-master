import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
