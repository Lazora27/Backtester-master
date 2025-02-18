import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
