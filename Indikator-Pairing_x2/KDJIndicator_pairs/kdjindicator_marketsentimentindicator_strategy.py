import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
