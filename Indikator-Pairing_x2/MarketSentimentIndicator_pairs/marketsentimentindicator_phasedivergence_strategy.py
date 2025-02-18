import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
