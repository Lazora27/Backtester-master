import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'DonchianChannels': 1.0
        })
    )
