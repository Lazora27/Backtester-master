import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'MovingAverage': 1.0
        })
    )
