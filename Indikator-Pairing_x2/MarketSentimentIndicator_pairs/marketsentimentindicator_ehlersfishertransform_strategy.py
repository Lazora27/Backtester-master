import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
