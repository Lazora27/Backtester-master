import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
