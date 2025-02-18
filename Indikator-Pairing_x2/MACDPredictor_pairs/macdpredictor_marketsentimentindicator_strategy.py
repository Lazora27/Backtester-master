import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
