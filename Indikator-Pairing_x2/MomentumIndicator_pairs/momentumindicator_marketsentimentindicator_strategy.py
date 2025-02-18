import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
