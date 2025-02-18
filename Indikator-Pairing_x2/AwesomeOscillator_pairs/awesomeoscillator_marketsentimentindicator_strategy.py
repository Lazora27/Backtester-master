import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
