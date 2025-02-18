import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
