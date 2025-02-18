import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
