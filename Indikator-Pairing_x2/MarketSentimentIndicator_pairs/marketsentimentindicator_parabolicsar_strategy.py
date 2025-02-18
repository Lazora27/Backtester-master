import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
