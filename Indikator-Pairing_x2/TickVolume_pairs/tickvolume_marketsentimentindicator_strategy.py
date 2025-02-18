import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
