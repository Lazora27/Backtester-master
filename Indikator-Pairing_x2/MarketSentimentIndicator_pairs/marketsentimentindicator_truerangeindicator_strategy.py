import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
