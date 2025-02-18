import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
