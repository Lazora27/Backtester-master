import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
