import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
