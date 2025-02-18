import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
