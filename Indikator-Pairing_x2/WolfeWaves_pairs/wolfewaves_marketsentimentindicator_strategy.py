import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
