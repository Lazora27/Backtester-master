import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
