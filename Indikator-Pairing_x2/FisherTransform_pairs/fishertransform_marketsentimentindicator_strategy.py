import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
