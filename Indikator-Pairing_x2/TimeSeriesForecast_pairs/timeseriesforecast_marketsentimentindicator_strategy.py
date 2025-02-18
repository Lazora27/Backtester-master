import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
