import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
