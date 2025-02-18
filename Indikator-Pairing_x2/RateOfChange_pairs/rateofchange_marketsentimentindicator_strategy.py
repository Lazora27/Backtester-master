import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
