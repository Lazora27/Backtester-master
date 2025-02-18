import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
