import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
