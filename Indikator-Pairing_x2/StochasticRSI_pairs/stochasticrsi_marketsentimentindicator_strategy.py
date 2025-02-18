import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
