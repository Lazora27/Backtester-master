import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_NormalizedAverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und NormalizedAverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'NormalizedAverageTrueRange': 1.0
        })
    )
