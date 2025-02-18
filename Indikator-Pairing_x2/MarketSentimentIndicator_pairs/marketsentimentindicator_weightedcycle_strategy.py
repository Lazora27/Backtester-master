import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
