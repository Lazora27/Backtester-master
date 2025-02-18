import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
