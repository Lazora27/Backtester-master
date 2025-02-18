import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
