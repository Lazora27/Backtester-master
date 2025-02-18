import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
