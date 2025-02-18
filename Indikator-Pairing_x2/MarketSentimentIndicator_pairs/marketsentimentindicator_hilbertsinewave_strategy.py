import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
