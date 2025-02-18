import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
