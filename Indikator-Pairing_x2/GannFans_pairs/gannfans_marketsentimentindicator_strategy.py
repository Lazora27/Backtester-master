import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
