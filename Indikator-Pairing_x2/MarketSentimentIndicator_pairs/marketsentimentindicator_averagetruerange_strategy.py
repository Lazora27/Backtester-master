import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
