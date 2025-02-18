import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
