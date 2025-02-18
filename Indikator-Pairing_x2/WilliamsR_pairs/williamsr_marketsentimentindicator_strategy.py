import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
