import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
