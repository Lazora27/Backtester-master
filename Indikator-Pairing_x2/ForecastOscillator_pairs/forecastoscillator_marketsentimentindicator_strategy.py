import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
