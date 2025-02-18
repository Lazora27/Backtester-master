import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
