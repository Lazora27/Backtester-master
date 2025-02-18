import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
