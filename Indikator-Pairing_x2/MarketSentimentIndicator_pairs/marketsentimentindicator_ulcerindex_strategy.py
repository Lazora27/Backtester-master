import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'UlcerIndex': 1.0
        })
    )
